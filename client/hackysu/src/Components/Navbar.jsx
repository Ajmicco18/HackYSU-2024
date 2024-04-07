import React from 'react';
import { Flex, Box, Text, Button, Image } from '@chakra-ui/react';

const Navbar = () => {
  return (
    <Flex
      as="nav"
      align="center"
      justify="space-between"
      padding="1rem"
      bg="blue.900"
      color="gold"
      position="sticky"
      top="0"
      zIndex="999" // Adjust z-index as needed
    >
      <Box maxW="33px">
        <a href="\">
          <Image src="Subject.png" alt="Logo" boxSize="50px" />
        </a>

      </Box>
      <Box>
        <a href="/">
          <Button variant="link" mr="4" color="gold">
            Home
          </Button>
        </a>
        <a href="/AboutPage">
          <Button variant="link" mr="4" color="gold">
            About
          </Button>
        </a>
        <a href="\ServicesPage">
          <Button variant="link" mr="4" color="gold">
            Services
          </Button>
        </a>
        <a href="\Contacts">
          <Button variant="link" color="gold">
            Contact
          </Button>
        </a>
      </Box>
    </Flex>
  );
}

export default Navbar;