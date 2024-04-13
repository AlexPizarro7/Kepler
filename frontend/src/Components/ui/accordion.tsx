import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';

const Accordion = ({ i, expanded, setExpanded, title, description }) => {
  const isOpen = i === expanded;

  return (
    <>
      <motion.div
        initial={false}
        animate={{
          backgroundColor: isOpen ? "black" : "#222",
          opacity: isOpen ? "50%":"100%",
        }}
        onClick={() => setExpanded(isOpen ? false : i)}
        style={{
          marginLeft: "2rem",
          marginRight: "2rem",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          padding: "2rem 4rem",
          cursor: "pointer"
        }}
      >
        {title}
      </motion.div>
      <AnimatePresence initial={false}>
        {isOpen && (
          <motion.section
            // Add animations for the accordion content
            initial="collapsed"
            animate="open"
            exit="collapsed"
            variants={{
              open: { opacity: 1, height: "auto",paddingTop:"2rem",paddingBottom:"2rem" },
              collapsed: { opacity: 0, height: 0,paddingTop:"0rem",paddingBottom:"0rem" },
            }}
            transition={{ duration: 0.4, ease: [0.04, 0.62, 0.23, 0.98] }}
            style={{
              marginLeft: "2rem",
              marginRight: "2rem",
              backgroundColor: "black",
              padding: "0 2rem",
            }}
          >
            {description}
          </motion.section>
        )}
      </AnimatePresence>
    </>
  );
};

export default Accordion;