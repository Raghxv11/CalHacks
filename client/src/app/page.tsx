import Image from "next/image";
import Hero from "@/components/Hero";
import DB from "@/components/db";
import About from "@/components/About";
import StarsCanvas from "@/components/canvas/Stars";
import TypewriterBox from "@/components/typewriter/TypewriterBox";

export default function Home() {
  return (
    <div>
      <Hero />
      {/* <TypewriterBox /> */}
      <div className="relative z-0">
        <DB />
        <StarsCanvas />
      </div>
      {/* <DB /> */}
      <div className="relative z-0">
        <About />
        <StarsCanvas />
      </div>
    </div>
  );
}
