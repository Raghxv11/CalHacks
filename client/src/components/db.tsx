// import React from "react";

// const DB: React.FC = () => {
//   return (
//     <div className="bg-[#00072D] h-screen">
//       <div className="flex flex-col items-center justify-center h-full">
//         <h1 className="text-[#F1F5F9] font-roboto text-4xl font-semibold mb-10">
//           Live Database
//         </h1>
//         <div className="flex flex-col items-start gap-4 p-[20px_32px] bg-[#1E1B4B] rounded-[16px]">
//           <ul className="flex flex-col gap-6">
//             <li className="flex gap-28">
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold w-48">
//                 Agent Address
//               </span>
//               <span className="text-[#6366F1] font-inter text-sm font-bold">
//                 GPU Cores
//               </span>
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold">
//                 RAM
//               </span>
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold">
//                 Availability
//               </span>
//                 <span className="text-[#86EFAC] font-roboto text-sm font-bold">
//                 Status
//               </span>
//             </li>
//             <div className="bg-[#475569] h-[1px]"></div>
//             <li className="flex gap-28">
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold w-48">
//                 Agent Address
//               </span>
//               <span className="text-[#6366F1] font-inter text-sm font-bold">
//                 GPU Cores
//               </span>
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold">
//                 RAM
//               </span>
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold">
//                 Availability
//               </span>
//               <span className="text-[#86EFAC] font-roboto text-sm font-bold">
//                 Status
//               </span>
//             </li>
//             <div className="bg-[#475569] h-[1px]"></div>
//             <li className="flex gap-28">
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold w-48">
//                 Agent ID
//               </span>
//               <span className="text-[#6366F1] font-inter text-sm font-bold">
//                 GPU Cores
//               </span>
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold">
//                 RAM
//               </span>
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold">
//                 Availability
//               </span>
//               <span className="text-[#86EFAC] font-roboto text-sm font-bold">
//                 Status
//               </span>
//             </li>
//             <div className="bg-[#475569] h-[1px]"></div>
//             <li className="flex gap-28">
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold w-48">
//                 Agent ID
//               </span>
//               <span className="text-[#6366F1] font-inter text-sm font-bold">
//                 GPU Cores
//               </span>
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold">
//                 RAM
//               </span>
//               <span className="text-[#F1F5F9] font-roboto text-sm font-bold">
//                 Availability
//               </span>
//               <span className="text-[#FCA5A5] font-roboto text-sm font-bold">
//                 Status
//               </span>
//             </li>
//           </ul>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default DB;

"use client";
import React, { useEffect, useState } from "react";
import TypewriterBox from "@/components/typewriter/TypewriterBox";

interface AgentData {
  agent_id: string;
  gpu_count: string;
  memory_gb: string;
  availability_hours: string;
  status: string;
}

const DB: React.FC = () => {
  const [agents, setAgents] = useState<AgentData[]>([]);

  // src/components/db.tsx
  useEffect(() => {
    // Ensure the URL matches your Flask server's address and port
    fetch("http://localhost:8080/api/data")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        const processedData = data.map((agent: any) => ({
          ...agent,
          status: parseInt(agent.gpu_count, 10) === 0 ? "Inactive" : "Active",
        }));
        setAgents(processedData);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <>
    <TypewriterBox /> 
    <div className="h-screen" id="db">
      <div className="flex flex-col items-center justify-center h-full">
        <h1 className="text-[#F1F5F9] font-roboto text-5xl font-semibold -mt-60 mb-10">
          Live Database
        </h1>
        <div className="flex flex-col items-start gap-4 p-[20px_32px] bg-[#100D25] rounded-[16px]">
          <ul className="flex flex-col gap-6">
            <li className="flex gap-28">
              <span className="text-[#F1F5F9] font-roboto text-sm font-bold w-48">
                Agent Address
              </span>
              <span className="text-[#6366F1] font-inter text-sm font-bold w-24 text-center">
                GPU Cores
              </span>
              <span className="text-[#F1F5F9] font-roboto text-sm font-bold w-24 text-center">
                RAM
              </span>
              <span className="text-[#F1F5F9] font-roboto text-sm font-bold w-32 text-center">
                Availability
              </span>
              <span className="text-[#F1F5F9] font-roboto text-sm font-bold w-24 text-center">
                Status
              </span>
            </li>
            <div className="bg-[#475569] h-[1px]"></div>
            {agents.map((data, index) => (
              <React.Fragment key={`${data.agent_id}-${index}`}>
                <li className="flex gap-28">
                  <span className="text-[#F1F5F9] font-roboto text-sm font-bold w-48">
                    {data.agent_id}
                  </span>
                  <span className="text-[#6366F1] font-inter text-sm font-bold w-24 text-center">
                    {data.gpu_count}
                  </span>
                  <span className="text-[#F1F5F9] font-roboto text-sm font-bold w-24 text-center">
                    {data.memory_gb}
                  </span>
                  <span className="text-[#F1F5F9] font-roboto text-sm font-bold w-32 text-center">
                    {data.availability_hours}
                  </span>
                  <span
                    className={`font-roboto text-sm font-bold w-24 text-center ${
                      data.status === "Active"
                        ? "text-[#86EFAC]"
                        : "text-[#FCA5A5]"
                    }`}
                  >
                    {data.status}
                  </span>
                </li>
                {index < agents.length - 1 && (
                  <div key={`separator-${index}`} className="bg-[#475569] h-[1px]"></div>
                )}
              </React.Fragment>
            ))}
          </ul>
        </div>
        </div>
      </div>
    </>
  );
};

export default DB;
