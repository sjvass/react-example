"use strict";


//class that specifies html to be rendered in
//StudentOptions tag
class StudentOptions extends React.Component {
    render() {
        //html list of links to pages
        return (
            <ul>
                <li>
                    <a href="/students">
                        Student List
                    </a>
                </li>
                <li>
                    <a href="/new-student">
                        Add New Student
                    </a>
                </li>
            </ul>
        )
    }
}



/* Method that renders your custom html tags 
    created ablove.
    - Takes these arguments in this order:
        (elements to be rendered, element to 
        where everything is to be rendered)
    - NOTE: can only render 1 tag, so if you
      have multiple elements, wrap them in a
      single div.
*/
ReactDOM.render(
    //custom html tags
    <div id="wrapper">
        <StudentOptions />
    </div>,
    //element where tags will be rendered
    document.getElementById('root')
);