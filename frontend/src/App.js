import { Outlet } from "react-router-dom";
import styled from "styled-components";

const Screen = styled.div`
  background-color: #e6e6e6;
  color: black;
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-height: 100vh; ;
`;

const Header = styled.header`
  align-items: center;
  background-color: #f6f6f6;
  border-bottom: 1px solid #dcdcdc;
  color: black;
  display: flex;
  justify-content: space-between;
  padding: 10px 20px;

  h1 {
    margin: 0;
  }
`;

const Main = styled.main`
  background-color: #f6f6f6;
  border-radius: 5px;
  margin: 10px;
  padding: 10px;
`;

const App = () => (
  <Screen>
    <Header>
      <h1>ЕВРАЗ</h1>
    </Header>
    <Main>
      <Outlet />
    </Main>
  </Screen>
);

export default App;
