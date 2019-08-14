import Axios from "axios";

const AUTHENTICATED = 'APP/AUTHENTICATED';
export const types = {AUTHENTICATED};

Axios.defaults.withCredentials = true;
const base_uri = 'http://localhost:8000';

export const authenticate = (data) => {
    Axios.get(base_uri+'/test-sess').then( resp => {
        console.log(resp)
    })
    return dispatch => {        
        console.log(data)
        Axios.post(base_uri + '/authenticate', data, {})
        .then( resp => {
            console.log(resp)
            dispatch(authenticated(resp.data))
        }).catch( err => {
            console.log(err)
        })
    }
}

const authenticated = (user) => {
    return {
        type: AUTHENTICATED,
        payload: {user}
    }
}