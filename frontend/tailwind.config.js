/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      backgroundImage: {
        'hero': 'url("/src/img/hero.jpg")',
        'mars': 'url("/src/img/mars.png")',
      }
    },
  },
  plugins: [],
}

