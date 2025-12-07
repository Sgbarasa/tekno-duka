import { Link } from "react-router-dom";

export default function ProductCard({ product }){
  return (
    <div style={{ width: 260 }}>
      <div className="card">
        <h4>{product.brand ? `${product.brand} ${product.model || product.name}` : product.name}</h4>
        {product.specs && <p className="small">{product.specs}</p>}
        <p><strong>Price:</strong> KES {product.price}</p>
        <p className="small">Stock: {product.stock ?? "N/A"}</p>
        <div style={{ display: "flex", gap: 8, marginTop: 8 }}>
          <Link to={`/product/${product.id}`} className="button">Details</Link>
        </div>
      </div>
    </div>
  );
}
