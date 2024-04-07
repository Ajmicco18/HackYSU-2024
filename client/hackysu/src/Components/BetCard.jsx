/* eslint-disable react/prop-types */
import { Card, /*CardHeader,*/ CardBody, /*CardFooter,*/ Image, Stack, Heading, Text, /*Divider, ButtonGroup, Button*/ } from '@chakra-ui/react'
//import { Link } from 'react-router-dom';
const BetCard = ({GameDay, GameTime, HomeTeam, MoneyLine1, VisitorTeam, Website}) => {
  const displayML = MoneyLine1
  return(
    <Card my = {'10px'}
    border={"1px 1px 1px 1px"}
    borderColor={"#232323"}
  direction={{ base: 'column', sm: 'row' }}
  overflow='hidden'
  variant='outline'
>
  <Image
    objectFit='cover'
    maxW={{ base: '100%', sm: '200px' }}
    src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/FedExForum_at_night.jpg/120px-FedExForum_at_night.jpg'
    alt='FedEx Forum'
  />

  <Stack>
    <CardBody marginLeft = {'15px'} my={'15px'}>
      <Heading size='md'>{HomeTeam + ' vs. ' + VisitorTeam}</Heading>

      <Text py='2'>
        The {HomeTeam} take on the {VisitorTeam} today, {GameDay}, at {GameTime}.
      </Text>
      <Text fontSize='xs' py='2'>
        
       {HomeTeam} {displayML} via {Website}
      </Text>
    </CardBody>
  </Stack>
</Card>
  )
}

export default BetCard;