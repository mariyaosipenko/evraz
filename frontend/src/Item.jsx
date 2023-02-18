import styled from "styled-components";
import { Button, Container } from "./components";

const Box = styled.div`
  display: flex;
  flex-direction: column;
`;

const Card = styled(Box)`
  margin-top: 12px;
  width: 49%;
`;

const Title = styled(Container)`
  align-items: center;
  background-color: dimgray;
  border-radius: 5px 5px 0 0;
  color: white;
  padding: 10px 20px;

  h4 {
    margin: 0;
  }
`;

const Content = styled(Box)`
  border: 1px solid #dcdcdc;
  border-radius: 0 0 5px 5px;
  padding: 20px;
`;

const Item = ({ data }) => (
  <Card>
    <Title>
      <h4>{`Эксгаустер ${data.name}`}</h4>
      <Button to={`/exhauster/${data.id}`}>&gt;</Button>
    </Title>
    <Content>Ротор</Content>
  </Card>
);

export default Item;
