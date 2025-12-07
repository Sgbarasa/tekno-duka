import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchAllProducts, fetchProducts } from "../api/api";
import ProductSpecs from "../components/ProductSpecs";
import { useCart } from "../context/CartContext";

export default function ProductDetails(){
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const { addToCart } = useCart();

  useEffect(() => {
    // Try to fetch single product via products endpoint by category or all products
    // Some backends expose GET /products/:id; if not, fallback to fetching all and finding by id
    fetchAllProducts()
      .then(list => {
        const found = list.find(p => String(p.id) === String(id));
        if (found) setProduct(found);
        else {
          // fallback: try to fetch products with no category then find
          fetchProducts().then(all => setProduct(all.find(p => String(p.id) === String(id))));
        }
      })
      .catch(err => console.error(err));
  }, [id]);

  if (!product) return <div className="container"><p>Loading product…</p></div>;

  return (
    <div className="container">
      <h2>{product.brand ? `${product.brand} ${product.model || product.name}` : product.name}</h2>
      <div style={{ display: "flex", gap: 16 }}>
        <div style={{ flex: 1 }}>
          <ProductSpecs product={product} />
          <div style={{ marginTop: 12 }}>
            <button className="button" onClick={() => addToCart(product, 1)}>Add to cart</button>
          </div>
        </div>
      </div>
    </div>
  );
}
