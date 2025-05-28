from flask import Flask, render_template

app = Flask(__name__)

@app.route('/email/')
@app.route('/email/<animal>')
def email(animal="Outro"):
    ticket = {
        'requester': {'first_name': 'João', 'name': 'João Silva'},
        'ticket_field_19408507869709': animal,
        'ticket_field_34060674472461': 'Dr. Pet',
        'ticket_field_34068936102669': 'Farmina N&D Prime Chicken',
        'ticket_field_34060757831821': 'https://exemplo.com/cupom',
        'assignee': {
            'custom_fields': {
                'link_do_calendly': 'https://calendly.com/farmina'
            }
        }
    }

    dc = {
        'fourth_greeting': 'tenha um ótimo dia!',
        'phone_template_email': '(11) 99999-9999',
        'whatsapp_template_email': '(11) 98888-8888',
        'email_template_email': 'contato@farmina.com',
        'template_button_calendly': 'Agende com nosso especialista',
        'calendly_template_email': 'https://calendly.com/farmina',
        'chatbot_template_email': 'Fale com nosso assistente virtual',
        'link_button_bot_ia': 'https://wa.me/5588999999999'
    }

    return render_template('email.html', ticket=ticket, dc=dc)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
