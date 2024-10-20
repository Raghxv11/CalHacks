"use client";
import React from "react";
import { motion } from "framer-motion";
import { SectionWrapper } from "../hoc";
import { styles } from "../styles";
import { EarthCanvas } from "./canvas";
import { slideIn } from "../utils/motion";

const About = () => {
  return (
    <div
      className={`xl:mt-12 flex xl:flex-row flex-col-reverse gap-10 overflow-hidden`}
      id="about"
    >
      <motion.div
        variants={slideIn("left", "tween", 0.2, 1)}
        className="flex-[0.75] bg-black-100 p-8 rounded-2xl"
      >
        <div className="mt-12 ml-32 bg-[#100D25] p-8 rounded-2xl">
          <h3
            className={`${styles.sectionHeadText} font-custom text-3xl md:text-4xl lg:text-5xl mt-4 mb-6`}
          >
            Our Story
          </h3>
          <p className="text-white text-lg mt-8">
            Imagine a world where innovation knows no bounds, where even the
            smallest startups can harness the power of advanced computational
            resources. While big tech companies spend millions of dollars on their GPU infrastructure, small
            developers and startups struggle to access the computational power
            needed to solve complex challenges, stifling creativity and limiting
            competition in an industry ripe for innovation. 
            <br /><br />
            Airpool is an
            open-source decentralized network that allows individuals to contribute their unused GPU resources. By pooling
            these resources, we create a shared infrastructure for distributing
            computational services that are accessible to small companies and
            developers. This empowers them to tackle sophisticated AI models and
            perform large-scale data analysis without heavy upfront
            investment in GPU hardware.
          </p>
        </div>
      </motion.div>

      <motion.div
        variants={slideIn("right", "tween", 0.2, 1)}
        className="xl:flex-1 xl:h-auto md:h-[550px] h-[350px]"
      >
        <EarthCanvas />
      </motion.div>
    </div>
  );
};

export default SectionWrapper(About, "about");
