(function() {
    var Register = this.Register = {};
    Register.p1 = undefined;
    Register.p2 = undefined;

    Register.validate_password = function() {
        var p1 = Register.p1.val();
        var p2 = Register.p2.val();
        Register.p2.parent().removeClass('has-error');
        Register.p2.tooltip('destroy');
        if (p1 != p2) {
            Register.p2.parent().addClass('has-error');
            Register.p2.tooltip({title: Register.p2.data("error"), placement: "bottom"});
            Register.p2.tooltip('show');
        }
    };

    Register.main = function() {
        Register.p1 = $("#id_password");
        Register.p2 = $("#id_password2");

        Register.p1.keyup(Register.validate_password);
        Register.p2.keyup(Register.validate_password);
    };

    Register.main();
}).call(this)
