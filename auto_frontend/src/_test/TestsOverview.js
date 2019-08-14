import React, { Component } from 'react';

class TestsOverview extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            // <TestForm handle_submit={this.handle_test_form_submit.bind(this)}/>
            <TestList tests={this.props.tests} />
        );
    }
    handle_test_form_submit(ev) {
        console.log(ev)
        const test_name = document.getElementById('testform-test_name').value, application_uri = document.getElementById('testform-application_uri').value, expected_text = document.getElementById('testform-expected_text').value, test_file = document.getElementById('testform-test_file').files[0];
        this.props.handle_create_test({ test_name, test_file, application_uri, expected_text })
    }
}

const TestForm = (props) => {
    return (<div>
        test name:<input type='text' id='testform-test_name' />
        application uri:<input type='text' id='testform-application_uri' />
        expected text:<input type='text' id='testform-expected_text' />
        test file:<input type='file' id='testform-test_file' />
        <button onClick={props.handle_submit}>submit</button>
    </div>)
}
const TestList = ({ tests }) => {
    console.log(tests)
    return (<div>
        {tests.map((el, i) => <TestListItem key={i} obj={el} />)}
    </div>)
}
const TestListItem = ({ obj }) => {
    console.log(obj)
    console.log('hello')
    return (<div>
        {obj.test_name}
    </div>)
}

export default TestsOverview;