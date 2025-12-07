import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import { CartProvider } from "./context/CartContext";

import Home from "./pages/Home";
import Categories from "./pages/Categories";
import CategoryProducts from "./pages/CategoryProducts";
import Products from "./pages/Products";         // <-- new page
import ProductDetails from "./pages/ProductDetails";
import Cart from "./pages/Cart";
import Orders from "./pages/Orders";

export default function App() {
  return (
    <CartProvider>
      <Router>
        <Navbar />
        <main style={{ padding: 16 }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/categories" element={<Categories />} />
            <Route path="/categories/:id" element={<CategoryProducts />} />
            <Route path="/products" element={<Products />} />      {/* <-- added */}
            <Route path="/product/:id" element={<ProductDetails />} />
            <Route path="/cart" element={<Cart />} />
            <Route path="/orders" element={<Orders />} />
          </Routes>
        </main>
      </Router>
    </CartProvider>
  );
}
