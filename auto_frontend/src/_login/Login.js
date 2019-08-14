import React, {Component} from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import * as actions from '../ducks/App/actions';

class Login extends Component{
    render(){
        return(<div>
            <p>username</p> <input type='text' id='loginform-username'/>
            <p>password</p> <input type='password' id='loginform-password'/>
            <button onClick={this.handle_login.bind(this)}>login</button>
        </div>)
    }
    handle_login(ev){
        const username = document.getElementById('loginform-username').value, password = document.getElementById('loginform-password').value;
        const data = {username, password};
        this.props.app_actions.authenticate(data);
    }
}

const mapStateToProps = (state) => ({app:state.App});
const mapActionsToProps = (dispatch) => ({app_actions:bindActionCreators(actions, dispatch)})
export default connect(mapStateToProps, mapActionsToProps)(Login);