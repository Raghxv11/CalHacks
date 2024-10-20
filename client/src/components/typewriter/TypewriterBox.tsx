"use client";
import React, { useEffect, useState } from "react";
import "./TypewriterBox.css"; // Your CSS for styling

const TypewriterBox: React.FC = () => {
  const [text, setText] = useState(""); // Holds the displayed text

  // The full text to be displayed, including LEAD and DONOR sections, formatted as paragraphs without line breaks
  const fullText = `
    LEAD: Hello, this is agent **vp0fnz! I am requesting GPU power for project named: “AI Model Training”. The number of GPUs required: 30. The required memory is: 64 GB. The task is “Training a large language model”. Let me know resource availability ASAP!

    Contributor 1: Hi, this is agent **7fcqcy! I can allocate GPU count of: 13. The memory I can allocate is: 32 GB. Please note that these allocations are available for: 12 hours.

    Contributor 2: Hi, this is agent **q5wv7h! I can allocate GPU count of: 10. The memory I can allocate is: 16 GB. Please note that these allocations are available for: 17 hours.

    Contributor 3: Hi, this is agent **rry2v5! I can allocate GPU count of: 9. The memory I can allocate is: 64 GB. Please note that these allocations are available for: 12 hours.

    Contributor 4: Hi, this is agent **sgwv85! I can allocate GPU count of: 15. The memory I can allocate is: 32 GB. Please note that these allocations are available for: 9 hours.

    Contributor 5: Hi, this is agent **2nsczr! I can allocate GPU count of: 13. The memory I can allocate is: 32 GB. Please note that these allocations are available for: 10 hours.
  `;

  useEffect(() => {
    let index = 0;

    // Interval to type out each character one at a time
    const interval = setInterval(() => {
      if (index < fullText.length) {
        setText((prev) => prev + fullText[index]);
        index++;
      } else {
        clearInterval(interval); // Stop when the text is fully typed out
      }
    }, 20); // Typing speed (adjust for faster/slower typing)

    return () => clearInterval(interval); // Cleanup the interval on component unmount
  }, [fullText]);

  return (
    <div className="container">
      <div className="e-card playing">
        <div className="image"></div>

        {/* Wave effects */}
        <div className="wave"></div>
        <div className="wave"></div>
        <div className="wave"></div>

        {/* Info top - Icon */}
        <div className="infotop">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            className="icon"
          ></svg>
        </div>

        {/* Typewriter effect text */}
        <div className="typewriter">
          <p>{text}</p>
        </div>
      </div>
    </div>
  );
};

export default TypewriterBox;
