$(function() {
  var $Form    = $('#content .box'),
      $username      = $Form.find('.username'),
      $password      = $Form.find('.new_pass'),
      $strengthMeter = $Form.find('.J_StrengthMeter'),
      $body          = $('body');


  $.strength($username, $password, function(user, pwd, strength){
    $strengthMeter
      .removeClass('weak')
      .removeClass('good')
      .removeClass('strong');
    if (strength.password.length) {
      $strengthMeter.addClass(strength.status);
    }
  });

});
