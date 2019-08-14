import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as actions from '../ducks/Test/actions';
import TestOverview from './TestsOverview';

class Test extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <TestOverview handle_create_test={this.handle_create_test.bind(this)} tests={this.props.test.tests}/>
        )
    }
    componentDidMount(){
        this.handle_get_tests();
    }

    handle_create_test(form_data) {
        console.log(form_data)
        this.props.test_api.create_test(form_data);
    }
    handle_get_tests(){
        this.props.test_api.get_tests();
    }

}
const mapStateToProps = (state) => ({test:state.Test});
const mapActionsToProps = (dispatch) => ({test_api:bindActionCreators(actions,dispatch)});
export default connect(mapStateToProps, mapActionsToProps)(Test);