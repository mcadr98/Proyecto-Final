import React from "react";
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from "react-router-dom";
import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

function LandingPage({ isLoggedIn }) {
  return (
    <div className="p-6 text-center">
      <h1 className="text-3xl font-bold">Bienvenido a PopcornHour</h1>
      <p className="mt-4">Explora y comparte tu amor por las películas y series.</p>
      {isLoggedIn ? (
        <Button asChild>
          <Link to="/home">Ir a la página principal</Link>
        </Button>
      ) : (
        <div className="flex justify-center gap-4 mt-6">
          <Button asChild>
            <Link to="/login">Iniciar sesión</Link>
          </Button>
          <Button asChild>
            <Link to="/signup">Registrarse</Link>
          </Button>
        </div>
      )}
    </div>
  );
}

function LoginPage({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {
    // Simulación de login
    if (email && password) {
      onLogin(true);
    }
  };

  return (
    <Card className="max-w-md mx-auto mt-10">
      <CardContent>
        <h2 className="text-xl font-bold text-center">Iniciar Sesión</h2>
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleLogin();
          }}
          className="flex flex-col gap-4 mt-6"
        >
          <Input
            type="email"
            placeholder="Correo electrónico"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <Input
            type="password"
            placeholder="Contraseña"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <Button type="submit">Iniciar sesión</Button>
        </form>
      </CardContent>
    </Card>
  );
}

function SignupPage({ onSignup }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = () => {
    // Simulación de registro
    if (email && password) {
      onSignup(true);
    }
  };

  return (
    <Card className="max-w-md mx-auto mt-10">
      <CardContent>
        <h2 className="text-xl font-bold text-center">Crear Cuenta</h2>
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSignup();
          }}
          className="flex flex-col gap-4 mt-6"
        >
          <Input
            type="email"
            placeholder="Correo electrónico"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <Input
            type="password"
            placeholder="Contraseña"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <Button type="submit">Registrarse</Button>
        </form>
      </CardContent>
    </Card>
  );
}

function HomePage() {
  return (
    <div className="p-6 text-center">
      <h1 className="text-3xl font-bold">Página Principal</h1>
      <p className="mt-4">¡Disfruta explorando las recomendaciones!</p>
    </div>
  );
}

export default function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={<LandingPage isLoggedIn={isLoggedIn} />}
        />
        <Route
          path="/login"
          element={<LoginPage onLogin={setIsLoggedIn} />}
        />
        <Route
          path="/signup"
          element={<SignupPage onSignup={setIsLoggedIn} />}
        />
        <Route
          path="/home"
          element={isLoggedIn ? <HomePage /> : <Navigate to="/login" />}
        />
      </Routes>
    </Router>
  );
}
