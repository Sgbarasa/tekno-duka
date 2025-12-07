import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: API_BASE,
  headers: { "Content-Type": "application/json" }
});

// Categories
export const fetchCategories = () => api.get("/categories/").then(r => r.data);

// Products
// backend supports GET /products/?category_id=ID, but we handle fallback
export const fetchProducts = (categoryId) =>
  api.get("/products/", { params: categoryId ? { category_id: categoryId } : {} }).then(r => r.data);

// get all products (helper)
export const fetchAllProducts = () => api.get("/products/").then(r => r.data);

// Orders
// backend expects one order per record: { customer_name, product_id, quantity }
export const createOrder = (order) => api.post("/orders/", order).then(r => r.data);
export const fetchOrders = () => api.get("/orders/").then(r => r.data);

export default api;
