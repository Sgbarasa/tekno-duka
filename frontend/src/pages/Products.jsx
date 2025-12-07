import { useEffect, useState } from "react";
import { fetchProducts } from "../api/api";
import ProductCard from "../components/ProductCard";

export default function Products() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchProducts()
      .then(setProducts)
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="container">
      <h2>All Products</h2>
      {products.length === 0 && <p>No products found.</p>}
      <div className="grid">
        {products.map(p => <ProductCard key={p.id} product={p} />)}
      </div>
    </div>
  );
}
