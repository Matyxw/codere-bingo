import { test, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import App from "../src/App";

test("muestra el título principal", () => {
  render(<App />);
  expect(screen.getByText("Codere Bingo")).toBeDefined();
});

test("muestra la página de compra", () => {
  render(<App />);
  expect(screen.getByText("Nueva compra")).toBeDefined();
});
