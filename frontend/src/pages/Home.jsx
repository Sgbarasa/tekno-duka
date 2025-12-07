import { Link } from "react-router-dom";

export default function Home(){
  return (
    <div className="container">
      <div className="card" style={{ padding: 24 }}>
        <h1>TeknoDuka</h1>
        <p>Browse, compare, and purchase electronics. Start by exploring categories or products.</p>
        <div style={{ marginTop: 12 }}>
          <Link to="/categories" className="button">Browse Categories</Link>
          <Link to="/products" className="button" style={{ marginLeft: 8, background: "#06b6d4" }}>View All Products</Link>
        </div>
      </div>
    </div>
  );
}
