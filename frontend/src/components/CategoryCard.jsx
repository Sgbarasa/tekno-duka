import { Link } from "react-router-dom";

export default function CategoryCard({ category }){
  return (
    <Link to={`/categories/${category.id}`} style={{ width: 240, textDecoration: "none" }}>
      <div className="card">
        <h3>{category.name}</h3>
        <p className="small">ID: {category.id}</p>
      </div>
    </Link>
  );
}
