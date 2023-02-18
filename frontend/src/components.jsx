import { Link } from "react-router-dom";
import styled from "styled-components";

export const Button = styled(Link)`
  align-self: center;
  background-color: #f6f6f6;
  border: 1px solid #dcdcdc;
  border-radius: 5px;
  color: dimgray;
  padding: 5px 10px;
  text-decoration: none;
`;

export const Container = styled.div`
  display: flex;
  justify-content: space-between;
`;
