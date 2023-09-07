from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(data):
    # Create a PDF document
    doc = SimpleDocTemplate("resume.pdf", pagesize=letter)

    # Create a list of flowables (content elements)
    story = []

    # Define a style for the heading
    styles = getSampleStyleSheet()
    heading_style = styles["Heading1"]

    # Add personal information
    story.append(Paragraph("Personal Information", heading_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"First Name: {data['firstname']}", styles["Normal"]))
    story.append(Paragraph(f"Last Name: {data['lastname']}", styles["Normal"]))
    story.append(Paragraph(f"Email: {data['email']}", styles["Normal"]))
    story.append(Paragraph(f"Phone Number: {data['phonenumber']}", styles["Normal"]))
    story.append(Paragraph(f"City: {data['city']}", styles["Normal"]))
    story.append(Paragraph(f"State: {data['state']}", styles["Normal"]))
    story.append(Spacer(1, 12))

    # Add education section
    story.append(Paragraph("Education", heading_style))
    story.append(Spacer(1, 12))
    for education in data["education"]:
        story.append(Paragraph(f"School Name: {education['schoolname']}", styles["Normal"]))
        story.append(Paragraph(f"Degree: {education['degree']}", styles["Normal"]))
        story.append(Paragraph(f"Start Date: {education['start_date']}", styles["Normal"]))
        story.append(Paragraph(f"End Date: {education['end_date']}", styles["Normal"]))
        story.append(Spacer(1, 12))

    # Add experience section
    story.append(Paragraph("Experience", heading_style))
    story.append(Spacer(1, 12))
    for experience in data["experience"]:
        story.append(Paragraph(f"Job Title: {experience['jobtitle']}", styles["Normal"]))
        story.append(Paragraph(f"Company: {experience['company']}", styles["Normal"]))
        story.append(Paragraph(f"Start Date: {experience['start_date']}", styles["Normal"]))
        story.append(Paragraph(f"End Date: {experience['end_date']}", styles["Normal"]))
        story.append(Spacer(1, 12))

    # Build the PDF document
    doc.build(story)
