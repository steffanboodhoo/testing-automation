import Axios from "axios";
const RECEIVE_TESTS = 'TEST/RECEIVE_TESTS';
export const types = {RECEIVE_TESTS};


const base_uri = 'http://localhost:8000';

export const get_tests = () => {
    const params = {};
    return dispatch => {
        Axios.get(base_uri + '/test', {
            params: params
        }).then(resp => {
            dispatch(receive_tests(resp.data))
        }).catch(err => {
            console.log(err)
        })
    }
}
const receive_tests = (tests) => {
    return {
        type: RECEIVE_TESTS,
        payload: {tests}
    }
}

export const create_test = (data) => {
    let form_data = new FormData();
    form_data.append('test_file', data.test_file), form_data.append('test_name', data.test_name), form_data.append('application_uri', data.application_uri), form_data.append('expected_text', data.expected_text);
    return dispatch => {
        Axios.post(base_uri + '/test', form_data, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }).then(resp => {
            console.log(resp)
        }).catch(err => {
            err
        })
    }
}