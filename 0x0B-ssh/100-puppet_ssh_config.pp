# set up client SSH configuration file with puppet.
file { '~/.ssh/config':
    ensure  => 'file',
    content => "
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
    ",
}
