<?php
// Verificar se os campos de usuário e senha foram enviados
if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Configurações do servidor RADIUS
    $radius_server = "endereco_do_servidor_radius";
    $radius_port = 1812; // Porta padrão do RADIUS
    $radius_secret = "segredo_compartilhado"; // Segredo compartilhado configurado no servidor RADIUS

    // Conexão com o servidor RADIUS
    $radius_handle = radius_auth_open();
    radius_add_server($radius_handle, $radius_server, $radius_port, $radius_secret, 5, 3); // Timeout de 5 segundos, até 3 tentativas

    // Realiza a autenticação
    $radius_response = radius_authenticate($radius_handle, $username, $password);

    // Fecha a conexão
    radius_close($radius_handle);

    // Verifica se a autenticação foi bem-sucedida
    if ($radius_response === RADIUS_ACCESS_ACCEPT) {
        // Autenticação bem-sucedida, redireciona para a página de sucesso
        header("Location: login_sucesso.php");
        exit();
    } else {
        // Autenticação falhou, redireciona para a página de erro
        header("Location: login_falhou.php");
        exit();
    }
}
?>
