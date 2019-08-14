import React, { Component } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

class Project extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <h1>Project</h1>
        )
    }
}
const mapStateToProps = (state) => ({});
const mapActionsToProps = (actions) => ({});
export default connect(mapStateToProps, mapActionsToProps)(Project);