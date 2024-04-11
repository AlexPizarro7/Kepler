"use client";
import React from "react";
import { StickyScroll } from "./ui/sticky-scroll-reveal";

const content = [
  {
    title: "How do I access the Kepler Astrological Calendar?",
    description:
      "Sign up or sign in today in order to view astrological events happening in your area.",
    content: (
      <div className="h-full w-full bg-[linear-gradient(to_bottom_right,#06b6d4,#10b981)] flex items-center justify-center text-white">
        Access our Calendar
      </div>
    ),
  },
  {
    title: "What is premium access?",
    description:
      "Premium access provides you the oportunity to access our special features and community events. Sign up today to learn more.",
    content: (
        <div className="h-full w-full bg-[linear-gradient(to_bottom_right,var(--orange-500),var(--yellow-500))] flex items-center justify-center text-white">
        Version control
      </div>
    ),
  },
  {
    title: "Version control",
    description:
      "Experience real-time updates and never stress about version control again. Our platform ensures that you're always working on the most recent version of your project, eliminating the need for constant manual updates. Stay in the loop, keep your team aligned, and maintain the flow of your work without any interruptions.",
    content: (
      <div className="h-full w-full bg-[linear-gradient(to_bottom_right,var(--orange-500),var(--yellow-500))] flex items-center justify-center text-white">
        Version control
      </div>
    ),
  },
  {
    title: "Running out of content",
    description:
      "Experience real-time updates and never stress about version control again. Our platform ensures that you're always working on the most recent version of your project, eliminating the need for constant manual updates. Stay in the loop, keep your team aligned, and maintain the flow of your work without any interruptions.",
    content: (
      <div className="h-full w-full bg-[linear-gradient(to_bottom_right,#06b6d4,#10b981)] flex items-center justify-center text-white">
        Running out of content
      </div>
    ),
  },
];
export function FAQReveal() {
  return (
    <div className="p-10">
      <StickyScroll content={content} />
    </div>
  );
}
