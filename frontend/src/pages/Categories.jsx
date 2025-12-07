import { useEffect, useState } from "react";
import { fetchCategories } from "../api/api";
import CategoryCard from "../components/CategoryCard";

export default function Categories(){
  const [cats, setCats] = useState([]);

  useEffect(() => {
    fetchCategories().then(setCats).catch(err => console.error(err));
  }, []);

  return (
    <div className="container">
      <h2>Categories</h2>
      <div className="grid">
        {cats.map(c => <CategoryCard key={c.id} category={c} />)}
      </div>
    </div>
  );
}
