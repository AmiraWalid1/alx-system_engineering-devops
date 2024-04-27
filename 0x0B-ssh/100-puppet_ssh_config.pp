# set up client SSH configuration file with puppet.
file { '~/.ssh/config':
    ensure  => 'file',
    path    =>  '/etc/ssh/ssh_config',
    content => "
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
    ",
}
