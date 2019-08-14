import React, { Component } from 'react';
import { BrowserRouter, Route, Redirect } from 'react-router-dom';


import Home from '../_home/Home';
import Project from '../_project/Project';
import Test from '../_test/Test';
import Login from '../_login/Login';

const PrivateRoute = ({ component: Component, app, ...props }) => {
    return (<Route {...props} render={props => {
        return (app.logged_in ? <Component {...props} /> : <Redirect to='/login' />)
    }} />)
}
const DefaultRoute = ({ component: Component, app, ...props }) => {
    return (<Route {...props} render={props => {
        return (app.logged_in ? <Redirect to='/home' /> : <Component {...props} />)
    }} />)
}

class App extends Component {
    render() {
        return (<BrowserRouter>
            <div>
                <Route path='/' exact={true} render={() => (<Home/>) }/>
                <Route path='/test' render={() => (<Test/>) }/>
                <Route path='/project' render={() => (<Project/>) }/>
                <Route path='/login' render={() => (<Login/>) }/>
            </div>
        </BrowserRouter>)
            }
        }

export default App;