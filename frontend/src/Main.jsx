import styled from "styled-components";
import { Container } from "./components";
import Item from "./Item";

const Card = styled.div`
  width: 32%;

  h3 {
    background-color: #fcba30;
    border-radius: 5px;
    color: dimgray;
    margin: 0;
    padding: 10px 20px;
  }
`;

const Machine = ({ entry }) => (
  <Card>
    <h3>{`Агломашина №${entry.id}`}</h3>
    <Container>
      <Item data={entry.ex[0]} />
      <Item data={entry.ex[1]} />
    </Container>
  </Card>
);

const Main = ({ data = MOCK }) => (
  <>
    <h2>Главный экран</h2>
    <Container>
      {data.map((entry) => (
        <Machine key={entry.id} entry={entry} />
      ))}
    </Container>
  </>
);

export default Main;

const MOCK = [
  {
    id: 1,
    ex: [
      { id: 10, name: "У-171", data: null },
      { id: 11, name: "У-172", data: null },
    ],
  },
  {
    id: 2,
    ex: [
      { id: 12, name: "Ф-171", data: null },
      { id: 13, name: "Ф-172", data: null },
    ],
  },
  {
    id: 3,
    ex: [
      { id: 14, name: "Х-171", data: null },
      { id: 15, name: "Х-172", data: null },
    ],
  },
];
