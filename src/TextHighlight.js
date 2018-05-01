/* Component for displaying the text as received from
*  the API and marking the words selected by the user.
*/

import React from 'react';

class TextHighlight extends React.Component{

    render(){
        if(!this.props.highlightWord) {
            return (
                <span>
                    {this.props.text}
                </span>
            );
        }
        const regex = new RegExp(`\\b(${this.props.highlightWord})\\b`, 'gi');
        const sections = this.props.text.split(regex);
        return (
            <div>
                { sections.map((section, i) => (
                    regex.test(section) ? 
                    <mark key={i}>
                        {section}
                    </mark> 
                    : 
                    <span key={i}>
                        {section}
                    </span>
                ))}
            </div>
        );
    }
}

export default TextHighlight;