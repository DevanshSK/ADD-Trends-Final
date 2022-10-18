import "../styles/globals.css";
import { StateContext } from "../lib/context";
import Navbar from "../components/Navbar";

function MyApp({ Component, pageProps }) {
  return (
    <StateContext>
      <Navbar />
      <Component {...pageProps} />
    </StateContext>
  );
}

export default MyApp;
