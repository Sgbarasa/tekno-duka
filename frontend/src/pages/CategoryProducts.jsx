import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { fetchProducts } from "../api/api";
import ProductCard from "../components/ProductCard";

export default function CategoryProducts(){
  const { id } = useParams();
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchProducts(id).then(setProducts).catch(err => console.error(err));
  }, [id]);

  return (
    <div className="container">
      <Link to="/categories">← Back to categories</Link>
      <h2>Products in category</h2>
      <div className="grid">
        {products.map(p => <ProductCard key={p.id} product={p} />)}
      </div>
    </div>
  );
}
