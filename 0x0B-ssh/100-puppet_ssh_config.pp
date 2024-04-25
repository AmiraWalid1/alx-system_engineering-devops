# set up client SSH configuration file with puppet.
class { 'ssh':
    client_options => {
        'Host *' => {
            'IdentityFile' => '~/.ssh/school',
            'PasswordAuthentication' => 'no',
        },
    },
}
