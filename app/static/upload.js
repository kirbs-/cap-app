$(document).ready(() => {
    // add upload button handler
    $('#upload-form-btn').click( evt => {
        // block link from processing
        evt.preventDefault();

        let $upload_form = $('#upload-form');

        // setup form data object to handle async multipart file upload.
        let form_data = new FormData();
        form_data.append('file', $('#file')[0].files[0]);

        // hide upload modal

        let url = $upload_form.attr('action');
        let method = $upload_form.attr('method');

        $.ajax({
            url: $upload_form.attr('action'), // grab url from form
            type: $upload_form.attr('method'), // grap request method from form
            data: form_data,
            processData: false,
            contentType: false,
            success: add_upload_file_row,
            // error: show_error_message,
        })

        $('#upload-modal').modal('hide');
    });

    // intercept display and stats link clicks and load display CSV via async
    // using the icon click we need to grab the url from the parent a tag
    $(document).on('click', '.glyphicon-th, .glyphicon-stats', evt => {
        // stop link click from propagating.
        evt.preventDefault();
        
        $.get({
            url: evt.target.parentElement.href, // grab url from event target's parent
            success: update_content_display,
        })
    });
    
});


// const upload_btn_handler = () => {
//     // Process upload button click via ajax.

//     // add a click event callback
    
// }

let add_upload_file_row = html => {
    // append HTML partial to 'main-table'
    $('#main-table').append(html);
}

let update_content_display = html => {
    // replace content table html
    let table = $('#content-table')
    table.html(html);

    // unhide div
    table.removeClass('hidden')

}