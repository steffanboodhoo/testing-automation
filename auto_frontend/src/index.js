import React from 'react';
import { render } from 'react-dom';

import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux'
import thunkMiddleware from 'redux-thunk';
import Axios from 'axios';
import RootReducer from './_app/RootReducer';

const store = createStore(
    RootReducer,
    applyMiddleware(thunkMiddleware)
)


// import 'materialize-css/dist/css/materialize.css'; //CSS
// import 'materialize-css'; //Only imports the javascript components
// import './common/common.css';
import App from './_app/App';


render(<Provider store={store}>
    <App />
</Provider>, document.getElementById('root'));