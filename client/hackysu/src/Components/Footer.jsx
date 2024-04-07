import React from 'react';
import { Box, Text } from '@chakra-ui/react';

const Footer = () => {
  return (
    <Box 
      as="footer" 
      bg="blue.900" 
      color="gold" 
      py="4" 
      textAlign="center" 
      fontFamily="Helvetica" // Setting the font family to Helvetica
    >
      <Text fontSize="sm">
        &copy; {new Date().getFullYear()} Company Name. All rights reserved.
      </Text>
    </Box>
  );
};

export default Footer;