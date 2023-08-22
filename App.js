// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import TrainSchedule from './components/TrainSchedule';
import TrainDetails from './components/TrainDetails';

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/" exact component={TrainSchedule} />
          <Route path="/train/:id" component={TrainDetails} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
