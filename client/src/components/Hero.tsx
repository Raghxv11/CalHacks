'use client'
import React, { useEffect, useState } from 'react';
import Navbar from './Navbar';

const Hero: React.FC = () => {
    const [offsetY, setOffsetY] = useState(0);

    const handleScroll = () => {
        setOffsetY(window.pageYOffset);
    };

    useEffect(() => {
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    return (
        <div
            className="bg-[url('/bg.jpg')] bg-cover bg-center w-full h-screen flex flex-col items-center"
            style={{ backgroundPositionY: `${offsetY * 0.5}px` }} // Parallax effect
        >
            <div className='mt-[28px] z-10 w-full'> {/* Updated class */}
                <Navbar />
            </div>
            <div className='flex flex-col justify-center items-center h-full -mt-[160px]'>
                <h1 className='text-[#F1F5F9] font-roboto text-[100px] font-black leading-none text-center'>The Future is Now</h1>
                <p className='text-[#F1F5F9] opacity-75 font-roboto text-2xl mt-[24px] font-normal leading-[125%]'>Democratizing Computational power: Empowering innovation for all.</p>
                <button className="w-[30px] h-[50px] rounded-full flex items-center justify-center bg-transparent border-none outline outline-2 outline-[#697FFF] shadow-[0_0_10px_#697FFF] absolute bottom-10" onClick={() => {
                    window.scrollTo({ top: window.innerHeight, behavior: 'smooth' });
                }}>
                    <div className="w-[5px] h-[10px] rounded-full bg-[#697FFF] shadow-[0_0_10px_#697FFF] animate-scroll"></div>
                </button>
            </div>
        </div>
    );
};

export default Hero;
