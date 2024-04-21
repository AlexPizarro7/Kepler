import React from "react";
import { BentoGrid, BentoGridItem } from "./ui/bento-grid";
import {
  IconArrowWaveRightUp,
  IconBoxAlignRightFilled,
  IconBoxAlignTopLeft,
  IconClipboardCopy,
  IconFileBroken,
  IconSignature,
  IconTableColumn,
} from "@tabler/icons-react";
 
export function FeatureSection() {
  return (
    <BentoGrid className="max-w-4xl mx-auto">
      {items.map((item, i) => (
        <BentoGridItem
          key={i}
          title={item.title}
          description={item.description}
          header={item.header}
          icon={item.icon}
          className={i === 3 || i === 6 ? "md:col-span-2" : ""}
        />
      ))}
    </BentoGrid>
  );
}
export default FeatureSection;

const Skeleton = () => (
  <div className="flex flex-1 w-full h-full min-h-[6rem] rounded-xl bg-gradient-to-br from-neutral-200 dark:from-neutral-900 dark:to-neutral-800 to-neutral-100"></div>
);

const items = [
  {
    title: "View the sun",
    description: "Witness the brilliance of our nearest star and learn about its fascinating dynamics.",
    header: <img src="/sun.jpg" />,
    icon: <IconClipboardCopy className="h-4 w-4 text-neutral-500" />,
  },
  {
    title: "View the moon",
    description: "Experience the beauty of Earth's natural satellite and explore its phases and features.",
    header: <img src="/moon.jpg" />,
    icon: <IconFileBroken className="h-4 w-4 text-neutral-500" />,
  },
  {
    title: "View the planets",
    description: "Discover the diverse worlds of our solar system, from the gas giants to the rocky surfaces of Mars and Venus.",
    header: <img src="/planet.jpg" />,
    icon: <IconSignature className="h-4 w-4 text-neutral-500" />,
  },
  {
    title: "View constellations",
    description:
      "Navigate the night sky and uncover the ancient stories behind the celestial patterns.",
    header: <img src="/stars.jpg" />,
    icon: <IconTableColumn className="h-4 w-4 text-neutral-500" />,
  },
  {
    title: "Subscribe to email newsletter",
    description: "Stay updated with the latest astronomical events, news, and offers straight to your inbox.",
    header: <img src="/eclipse.webp" />,
    icon: <IconArrowWaveRightUp className="h-4 w-4 text-neutral-500" />,
  },
  {
    title: "Contact us",
    description: "Have questions or need assistance? Reach out to our team for prompt support and guidance.",
    header: <img src="/kepler_telescope.jpg" />,
    icon: <IconBoxAlignTopLeft className="h-4 w-4 text-neutral-500" />,
  },
  {
    title: "Write a review",
    description: "Share your thoughts and feedback to help us improve and inspire others to explore the cosmos.",
    header: <img src="/shuttle.jpg" />,
    icon: <IconBoxAlignRightFilled className="h-4 w-4 text-neutral-500" />,
  },
];