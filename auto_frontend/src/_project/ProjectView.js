import Project from "./Project";

export const ProjectView = (props) => {
    return (
        <div>
            <h1>{props.name}</h1>
            <p>{props.description}</p>
            <div>{props.tests.map( (obj,i) => {
                return (<h3 key={i}>{obj.test_name}</h3>)
            })

            }</div>
        </div>
    )
}