import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import {
  ChakraProvider,
  createSystem,
  defaultConfig,
} from '@chakra-ui/react';
import './App.css';

const system = createSystem(defaultConfig);

function Home() {
  return (
    <div className="home">
      <h1>{{cookiecutter.project_name}}</h1>
      <p>{{cookiecutter.description}}</p>
    </div>
  );
}

function App() {
  return (
    <ChakraProvider value={system}>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </Router>
    </ChakraProvider>
  );
}

export default App;
