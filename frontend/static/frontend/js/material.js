import {MDCDialog} from '@material/dialog';

try {
    const dialog = new MDCDialog(document.querySelector('#pricing-guide-dialog'));

    document.querySelector('#pricing-guide-dialog-trigger').addEventListener('click', function () {
        dialog.show();
    });
} catch (e) {

}
