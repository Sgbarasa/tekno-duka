import React, { createContext, useContext, useState } from "react";

const CartContext = createContext();

export function CartProvider({ children }) {
  const [cart, setCart] = useState([]); // { id, name, price, quantity, ... }

  const addToCart = (product, qty = 1) => {
    setCart(prev => {
      const found = prev.find(p => p.id === product.id);
      if (found) {
        return prev.map(p => p.id === product.id ? { ...p, quantity: p.quantity + qty } : p);
      }
      return [...prev, { ...product, quantity: qty }];
    });
  };

  const updateQuantity = (id, qty) => {
    setCart(prev => prev.map(p => p.id === id ? { ...p, quantity: qty } : p));
  };

  const removeFromCart = (id) => {
    setCart(prev => prev.filter(p => p.id !== id));
  };

  const clearCart = () => setCart([]);

  const total = cart.reduce((s, it) => s + (Number(it.price || 0) * it.quantity), 0);

  return (
    <CartContext.Provider value={{ cart, addToCart, updateQuantity, removeFromCart, clearCart, total }}>
      {children}
    </CartContext.Provider>
  );
}

export const useCart = () => useContext(CartContext);
