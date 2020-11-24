// EPISODE CARD LOGIC
$('.epi-expand-btn').on('click', function()
{
        // Logic to close opend card -> close
    let all = $('.epi-expand-btn');
    for(let i=0; i<all.length ;i++){
        // Closing Opened Card
        if(all[i].getAttribute('aria-expanded')==='true' && all[i] !== this) {
            all[i].click()
        }
    }
    // Icon Rotation Logic
    invertIcon(this)

    let checkForExtraText = this.getAttribute('href')
    console.log(checkForExtraText)
    // Check If It has extra text
    if (checkForExtraText.search(',') !== -1){
        // If Has

        // Text Truncate logic
        let $parent = $($(this).parent().parent());
        let $firstText = $($('h5', $parent)[0]);
        let value = $firstText.text()

        // Adding ... Logic
        console.log($firstText.text())
        if ($firstText.text().search('…') !== -1) {
            value = value.slice(0, $firstText.text().length -1);
            $firstText.text(value);
        }
        // When Collapsing add ...
        else $firstText.text(value+ '…')
    }
});

function invertIcon(elementThis) {
        // Icon Rotation Logic
    let $iTag = $($('i', elementThis)[0]);
    let val  = $iTag[0].style.transform;
    val.replace('deg', '');
    val = val.replace('rotate(', '');
    val = parseInt(val.replace(')', ''))
    if (isNaN(val) || val !== 180) val = 180;
    else val = 0;

    $iTag.css('transform', 'rotate(' + val.toString() + 'deg)');
    console.log( $iTag[0].style.transform)


}