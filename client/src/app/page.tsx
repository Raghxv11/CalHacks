import Image from "next/image";
import Hero from "@/components/Hero";
// import Convo from "@/components/Convo";
import DB from "@/components/db";
import About from "@/components/About";
import StarsCanvas from "@/components/canvas/Stars";

export default function Home() {
  return (
    <div>
      <Hero />
      {/* <Convo /> */}
      <DB />
      <div className="relative z-0">
        <About />
        <StarsCanvas />
      </div>
    </div>
  );
}
