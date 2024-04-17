"use client";
import React from "react";
import {
  GlowingStarsBackgroundCard,
  GlowingStarsDescription,
  GlowingStarsTitle,
} from "./ui/glowing-stars";
 
export function StarsTest() {
  return (
      <div className="flex py-20 items-center justify-center antialiased">
        <GlowingStarsBackgroundCard>
          <GlowingStarsTitle>About Kepler</GlowingStarsTitle>
          <div className="flex justify-between items-end">
            <GlowingStarsDescription>
              Learn our mission is and what we have planned for the future.
            </GlowingStarsDescription>
            <div className="h-8 w-8 rounded-full bg-[linear-gradient(110deg,#333_0.6%,#222)] flex items-center justify-center" >
              <a href="/about-us"><Icon /></a>
            </div>
          </div>
        </GlowingStarsBackgroundCard>
      </div>
  );
}
 
const Icon = () => {

  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke-width="1.5"
      stroke="currentColor"
      className="h-4 w-4 text-white stroke-2"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        d="M17.25 8.25L21 12m0 0l-3.75 3.75M21 12H3"
      />
    </svg>
  );
};

export default StarsTest;